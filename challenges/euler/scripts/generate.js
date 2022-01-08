const inquirer = require('inquirer');
const fs = require('fs');
const path = require('path');
const { src } = require('../constants');
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
        }
    ])
    .then(async ({ problemNumber }) => {
        const problemName = problems[problemNumber - 1];

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
                path.join(src, `${problemNumber} - ${problemName}.ts`),
                `${problemContent}
export = {};

// Output
console.log();`
            );
        });
    });
