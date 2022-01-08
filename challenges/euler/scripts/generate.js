const inquirer = require('inquirer');
const fs = require('fs');
const path = require('path');
const { src, thoughts: thoughtsDir } = require('../constants');
const axios = require('axios');
const cheerio = require('cheerio');

const problems = fs
    .readFileSync(path.join(__dirname, '..', 'readme.md'))
    .toString()
    .match(/^-   \[.] (?:\[(.*)\]|(.*))/gm)
    .map(res => {
        const sanitised = res.substring(8).replace('[', '').replace(']', '');
        return sanitised.match(/[0-9]* - (.*)/)[1];
    });

inquirer
    .prompt([
        {
            name: 'problemNumber',
            message: 'Which problem would you like to solve?',
            type: 'number',
            validate: input =>
                parseInt(input) > 100
                    ? 'Please make sure you choose a number between 1 and 100!'
                    : true
        },
        {
            name: 'thoughts',
            message: 'Should I generate a thoughts document for you?',
            type: 'confirm',
            default: false
        }
    ])
    .then(async ({ problemNumber, thoughts }) => {
        const fileName = `${problemNumber} - ${problems[problemNumber - 1]}`;

        // Fetch the problem data off of projecteuler.net
        axios.get(`https://projecteuler.net/problem=${problemNumber}`).then(({ data }) => {
            const $ = cheerio.load(data);
            const problemContent = $('.problem_content')
                .text()
                .trim()
                .split('\n')
                .map(r => `// ${r}`)
                .join('\n');

            fs.writeFileSync(
                path.join(src, `${fileName}.ts`),
                `${problemContent}
export = {};

// Output
console.log();`
            );

            if (thoughts) fs.writeFileSync(path.join(thoughtsDir, `${fileName}.md`), '');
        });
    });
