import fs from 'fs';
const file = "./test.txt";
function readFileContent() {
    const reading = fs.readFileSync(file, 'utf8');
    console.log(reading);
}
   
readFileContent(); 


function writeFileContent() {
    const writing = fs.writeFileSync(file , 'this is the new content for the file', 'utf8');
    console.log(readFileContent());
}
writeFileContent()