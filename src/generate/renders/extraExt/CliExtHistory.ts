/* ---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *-------------------------------------------------------------------------------------------- */

import * as fs from 'fs';
import { CodeModelAz } from '../../codemodel/CodeModelAz';
import * as path from 'path';
import { TemplateBase } from '../TemplateBase';
import { PathConstants } from '../../../utils/models';

export class CliExtHistory extends TemplateBase {
    constructor(model: CodeModelAz) {
        super(model);
        this.relativePath = PathConstants.historyRstFile;
        this.tmplPath = path.join(
            PathConstants.templateRootFolder,
            PathConstants.historyRstFile + PathConstants.njxFileExtension,
        );
    }

    public async fullGeneration(): Promise<string[]> {
        const { configHandler } = this.model.GetHandler();
        if (fs.existsSync(path.join(configHandler.azOutputFolder, this.relativePath))) {
            this.skip = true;
        } else {
            return this.render();
        }
    }

    public async incrementalGeneration(base: string): Promise<string[]> {
        return await this.fullGeneration();
    }

    public async GetRenderData(model: CodeModelAz): Promise<unknown> {
        return {};
    }
}
