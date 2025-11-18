import { useState } from "react";

const Calculate = ()=> {
const [num1 , setNum1] = useState("")
const [num2 , setNum2] = useState("")
const[operator, setOperator] = useState("+")
const[result , setResult] = useState(null)


function updateNum1(e){
    setNum1(
        e.target.value
    );
}
function updateNum2(e){
    setNum2(e.target.value);
}
function updateOperator(e){
    setOperator(e.target.value);
}

function calculateResult(){
    var n1 = Number(num1);
    var n2 = Number(num2);
    var answer = 0;

    switch(operator){
        case "+": answer = n1 + n2 ;
        break;

        case "-": answer = n1 - n2 ;
        break;

        case "*": answer = n1 * n2;
        break;

        case "/": answer = n1 / n2;
        break;

        
    }
    setResult(answer)

    
}




return (
  <div className="calc-container">

    <input
      placeholder="Enter first number"
      className="firstnumberinput"
      value={num1}
      type="number"
      onChange={updateNum1}
    />

    <select
      className="operatordropdown"
      value={operator}
      onChange={updateOperator}
    >
      <option value="+">+</option>
      <option value="-">-</option>
      <option value="*">×</option>
      <option value="/">÷</option>
    </select>

    <input
      placeholder="Enter second number"
      className="secondnumberinput"
      value={num2}
      type="number"
      onChange={updateNum2}
    />

    <button className="equalsbtn" onClick={calculateResult}>
      CALCULATE
    </button>

    <h2 className="resultlabel">{result}</h2>

  </div>
);


}
export default Calculate ;