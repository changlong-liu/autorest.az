﻿/* ---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *-------------------------------------------------------------------------------------------- */

import {
    CodeGenConstants,
    AzConfiguration,
    getHiddenOperations,
    groupOperations,
    RPInfo,
    isTrack2,
} from '../helper';
import * as fs from 'fs';
import { CodeModel } from '@azure-tools/codemodel';

function usePathVariable(p: string): string {
    const cliFolder = AzConfiguration.getValue(CodeGenConstants.azureCliFolder);
    const cliExtensionFolder = AzConfiguration.getValue(CodeGenConstants.azureCliExtFolder);
    const azOutputFolder = AzConfiguration.getValue(CodeGenConstants.azOutputFolder);
    if (p.startsWith(cliFolder) && p !== cliFolder) {
        p = `$(azure-cli-folder)${p.slice(cliFolder.length)}`;
    } else if (p.startsWith(cliExtensionFolder) && p !== cliExtensionFolder) {
        p = `$(azure-cli-extension-folder)${p.slice(cliExtensionFolder.length)}`;
    } else if (p.startsWith(azOutputFolder) && p !== azOutputFolder) {
        p = `$(az-output-folder)${p.slice(azOutputFolder.length)}`;
    }
    p = p.split('\\').join('/');
    return p;
}

function genBasicInfo(output: string[]) {
    output.push('');
    output.push('');
    output.push('## Azure CLI');
    output.push('');
    output.push('These settings apply only when `--az` is specified on the command line.');
    output.push('');
    output.push('``` yaml $(az)');
    const azConfig: Record<string, any> = AzConfiguration.getValue(CodeGenConstants.az);
    output.push('az:');
    output.push(`  extensions: ${azConfig[CodeGenConstants.extensions]}`);
    output.push(`  namespace: ${azConfig[CodeGenConstants.namespace]}`);
    output.push(`  package-name: ${azConfig[CodeGenConstants.packageName]}`);
    output.push(`  disable-checks: true`);
    output.push(`  randomize-names: true`);
    output.push(`  test-unique-resource: true`);
    output.push(
        `az-output-folder: ${usePathVariable(
            AzConfiguration.getValue(CodeGenConstants.azOutputFolder),
        )}`,
    );
    output.push(
        `python-sdk-output-folder: "${usePathVariable(
            AzConfiguration.getValue(CodeGenConstants.pythonSdkOutputFolder),
        )}"`,
    );
    output.push(
        `compatible-level: ${
            isTrack2(azConfig[CodeGenConstants.packageName]) ? 'track2' : 'track1'
        }`,
    );
    output.push('```');
}

const startTagLine = '### -----start of auto generated cli-directive----- ###';
const endTagLine = '### -----end of auto generated cli-directive----- ###';

function findGenArea(output: string[]): [number, number] {
    let start = -1,
        end = -1;
    for (let i = 0; i < output.length; i++) {
        if (start < 0 && output[i].indexOf(startTagLine) >= 0) start = i;
        if (output[i].indexOf(endTagLine) >= 0) end = i;
    }
    return [start, end];
}

export function GenerateReadmeAz(
    model: CodeModel,
    generateTargets: RPInfo,
    fullPath: string,
): string[] {
    const output: string[] = [];
    let alreadyExists = false;
    if (!fs.existsSync(fullPath)) {
        genBasicInfo(output);
    } else {
        output.push(...fs.readFileSync(fullPath).toString().split('\n'));
        alreadyExists = true;
    }

    let missingOps;
    if (alreadyExists) {
        missingOps = getHiddenOperations(model, generateTargets);
    } else {
        missingOps = [];
        for (const resourceInfo of generateTargets.resources) {
            missingOps.push(...resourceInfo.operations);
        }
    }

    if (missingOps.length > 0) {
        let area = findGenArea(output);
        if (area[1] <= 0) {
            output.push(``);
            output.push(startTagLine);
            output.push('``` yaml $(az)');
            output.push(`cli:`);
            output.push(`  cli-directive:`);
            if (!alreadyExists) {
                output.push(`    - where:`);
                output.push(`        group: '*'`);
                output.push(`        op: '*'`);
                output.push(`      hidden: true`);
            }
            output.push('```');
            output.push(endTagLine);
            area = findGenArea(output);
        }
        const grouped = groupOperations(missingOps);
        const newDirective = [];
        for (const groupName in grouped) {
            for (const version in grouped[groupName]) {
                const ops = grouped[groupName][version].map((x) => {
                    return x.operationName;
                });
                newDirective.push('    - where:');
                if (groupName !== '') newDirective.push(`        group: '${groupName}'`);
                newDirective.push(`        op: ${ops.join('|')}`);
                newDirective.push(`        apiVersion: '${version}'`);
                newDirective.push(`      hidden: false`);
            }
        }
        output.splice(area[1] - 1, 0, ...newDirective);
    }

    fs.writeFileSync(fullPath, output.join('\n'));
    return output;
}