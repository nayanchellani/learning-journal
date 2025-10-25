function modulesFunction() {
console.log('This is modules.js');
}

// export default modulesFunction; correct
// export { modulesFunction }; // also correct
//modules.exports.modulesFunction = modulesFunction; // works in CommonJS but not ES6