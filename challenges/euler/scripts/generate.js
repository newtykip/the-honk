const inquirer = require('inquirer');
const fs = require('fs');
const path = require('path');
const { root, src, thoughts: thoughtsDir } = require('../constants');
const axios = require('axios');
const cheerio = require('cheerio');
const chalk = require('chalk');

process.argv.shift();
process.argv.shift();

const readmeContent = fs.readFileSync(path.join(root, 'readme.md')).toString();

const problems = readmeContent.match(/^-   \[.] (?:\[(.*)\]|(.*))/gm).map(res => {
    const sanitised = res.substring(8).replace('[', '').replace(']', '');
    return sanitised.match(/[0-9]* - (.*)/)[1];
});

const questions = [];

if (isNaN(process.argv[0]))
    questions.push({
        name: 'problemNumber',
        message: 'Which problem would you like to solve?',
        type: 'number',
        validate: input => {
            input = parseInt(input);

            let alreadyGenerated = false;
            fs.readdirSync(src).forEach(file => {
                if (file.startsWith(input)) alreadyGenerated = true;
            });

            if (alreadyGenerated) return 'Please choose a problem you have not already completed!';
            else return true;
        }
    });

inquirer
    .prompt([
        ...questions,
        {
            name: 'thoughts',
            message: 'Should I generate a thoughts document for you?',
            type: 'confirm',
            default: false
        }
    ])
    .then(({ problemNumber, thoughts }) => {
        if (!problemNumber) problemNumber = parseInt(process.argv[0]);
        const fileName = `${problemNumber} - ${problems[problemNumber - 1]}`;

        // Fetch the problem data off of projecteuler.net
        axios
            .get(`https://projecteuler.net/problem=${problemNumber}`)
            .then(({ data }) => {
                const $ = cheerio.load(data);
                const problemContent = $('.problem_content')
                    .text()
                    .trim()
                    .split('\n')
                    .map(r => `// ${r}`)
                    .join('\n');

                // Generate the source file
                fs.writeFileSync(
                    path.join(src, `${fileName}.ts`),
                    `${problemContent}
export = {};

// Output
console.log();`
                );

                // Generate the thoughts file
                if (thoughts)
                    fs.writeFileSync(
                        path.join(thoughtsDir, `${fileName}.md`),
                        `<div align="center">

### ${problems[problemNumber - 1]}
</div>`
                    );

                // Check it off in the readme
                const regex = new RegExp(`   \\[.\\] ${problemNumber} - .*`);
                const match = readmeContent.match(regex);

                let newLine = `   [x] [${match[0]
                    .replace('[ ]', '')
                    .trim()}](src/${encodeURIComponent(fileName)}.ts)`;

                if (thoughts)
                    newLine += `\n    -   [Thoughts](thoughts/${encodeURIComponent(fileName)}.md)`;

                const newContent = readmeContent.replace(regex, newLine);

                fs.writeFileSync(path.join(root, 'readme.md'), newContent);

                // If the problem's ID is greater than 100, add it to the gitignore
                if (problemNumber > 100) {
                    const gitignorePath = path.join(root, '.gitignore');
                    const gitignoreContent = fs.readFileSync(gitignorePath).toString();
                    let newContent = `${gitignoreContent}\nsrc/${fileName}.ts`;
                    if (thoughts) newContent += `\nthoughts/${fileName}.md`;

                    fs.writeFileSync(gitignorePath, newContent);
                }
            })
            .catch(() =>
                console.error(
                    chalk.red(
                        chalk.bold(
                            'There was an error generating files for that challenge - please ensure that it exists on Project Euler!'
                        )
                    )
                )
            );
    });
