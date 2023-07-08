let {PythonShell} = require('python-shell')


// let options = {
//    mode: 'text',
//    pythonPath: '/Users/venuscheung/Library/CloudStorage/OneDrive-connect.hku.hk/year2sem1/sailing/googlemap001/interactive_map/005/',
//    pythonOptions: ['-u'], // get print results in real-time
//    scriptPath: '/Users/venuscheung/Library/CloudStorage/OneDrive-connect.hku.hk/year2sem1/sailing/googlemap001/interactive_map/005/',
//    args: ['hsign']
// };


//PythonShell.run('readwavefield.py', options).then(messages=>{
//  console.log('finished');
//});


PythonShell.runString('x=1+1;print(x)', null).then(messages=>{
  console.log('finished');
});

// const { readFileSync } = require("fs");
// var netcdfjs = require("netcdfjs")
//import NetCDFReader from '../index.js'

// const data = readFileSync("wavm-inner_wave.nc");

//let reader = new NetCDFReader(data);

// var reader = new NetCDFReader(data); // read the header
// reader.getDataVariable("hsign"); // go to offset and read it

// temperature-listener.js

const { spawn } = require('child_process');
const temperatures = []; // Store readings

const sensor = spawn('python', ['sensor.py']);
sensor.stdout.on('data', function(data) {
    
    // Coerce Buffer object to Float
    temperatures.push(parseFloat(data));

    // Log to debug
    console.log(temperatures);
});