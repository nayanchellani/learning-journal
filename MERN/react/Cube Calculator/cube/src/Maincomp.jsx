import { useState } from "react";

const Cubecalc = () => {
  const [num, setNum] = useState(0);
  const [result, setResult] = useState(0);
  function updateNum(e) {
    setNum(e.target.value);
  }
  function updateResult() {
    let ans;
    setResult((ans = Number(num) * Number(num) * Number(num)));
  }
  return (
    <>
      <input value={num} onChange={updateNum}></input>
      <button onClick={updateResult}>CALCULATE CUBE</button>

      <h1>{result}</h1>
    </>
  );
};
export default Cubecalc;
