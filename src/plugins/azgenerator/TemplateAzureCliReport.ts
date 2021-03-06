﻿/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

import { CodeModelAz } from "./CodeModelAz"
import { ParameterLocation } from "@azure-tools/codemodel";

export function GenerateAzureCliReport(model: CodeModelAz) : string[] {
    var output: string[] = [];

    output.push("# Azure CLI Module Creation Report");
    output.push("");

    let cmds = {};
    
    if (model.SelectFirstCommandGroup())
    {
        do
        {
            var mo: string[] = [];
            /*mo.push("## " + model.Command_Name);
            mo.push("");*/

            if (model.SelectFirstCommand())
            {
                do
                {
                    mo = getCommandBody(model);
                    cmds[model.Command_Name] = mo;
                    if(model.Command_CanSplit) {
                        mo = getCommandBody(model, true);
                        cmds[model.Command_Name.replace(/ create/g, " update")] = mo;
                    }
                }
                while (model.SelectNextCommand());
            }
            
        } while (model.SelectNextCommandGroup());;
    }
    // build sorted output
    var keys = Object.keys(cmds);
    keys.sort();

    for (var i = 0; i < keys.length; i++)
    {
        output = output.concat(cmds[keys[i]]);
    } 

    return output;
}

function getCommandBody(model: CodeModelAz, needUpdate: boolean = false) {
    let mo: string [] = [];
    if(needUpdate) {
        mo.push("### " + model.Command_Name.replace(/ create/g, " update"));
    } else {
        mo.push("### " + model.Command_Name);
    } 
    mo.push("");
    if(needUpdate) {
        mo.push(model.Command_MethodName.replace(/_create/g, "_update") + " a " + model.CommandGroup_Name +  ".");
    } else {
        mo.push(model.Command_MethodName + " a " + model.CommandGroup_Name +  ".");
    }
    
    mo.push("");

    mo.push("|Option|Type|Description|Path (SDK)|Path (swagger)|");
    mo.push("|------|----|-----------|----------|--------------|");


    if(!model.SelectFirstOption()) {
        return mo;
    }

    // first parameters that are required
    do
    {
        if (model.Option_In != ParameterLocation.Path && model.Option_IsRequired)
        {
            mo.push("|**--" + model.Option_Name + "**|" + model.Option_Type + "|" + model.Option_Description + "|" + model.Option_PathSdk + "|" + model.Option_PathSwagger + "|");
        }
    }
    while (model.SelectNextOption());

    if(!model.SelectFirstOption()) {
        return mo;
    }

    // following by required parameters
    do {
        if (model.Option_In != ParameterLocation.Path && !model.Option_IsRequired)
        {
            mo.push("|--" + model.Option_Name + "**|" + model.Option_Type + "|" + model.Option_Description + "|" + model.Option_PathSdk + "|" + model.Option_PathSwagger + "|");
        }
    }
    while (model.SelectNextOption());


    if (model.SelectFirstExample())
    {
        do
        {
            mo.push("");
            mo.push ("**Example: " + model.Example_Title + "**");
            mo.push("");
            mo.push("```");

            let next: string = model.Command_Name + " " + model.Command_MethodName + " ";
            if(needUpdate) {
                next = model.Command_Name.replace(/ create/g, " update") + " " + model.Command_MethodName.replace(/_create/g, "_update") + " ";
            }
            for (let k in model.Example_Params)
            {
                let v: string = model.Example_Params[k];
                if (/\s/.test(v))
                {
                    v = "\"" + v.replace("\"", "\\\"") + "\"";
                }

                next += k + " " + v;
                mo.push(next);
                next = "        ";
            }
            mo.push("```");
        } while (model.SelectNextExample());
    }
    return mo;     
}