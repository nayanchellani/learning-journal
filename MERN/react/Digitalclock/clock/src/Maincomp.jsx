import { useEffect, useState } from "react";

const DigiClock = () => {
  const [time, setTime] = useState("");
  const [date, setDate] = useState("");

  useEffect(() => {
    const id = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
    }, 1000);
    return()=> clearInterval(id)
  },[]);
  useEffect(() => {
    const id2 = setInterval(() => {
      setDate(new Date().toLocaleDateString());
    }, 1000);
    return()=> clearInterval(id2)
  },[]);

  return (
    <>
      <h1 className="timeContainer">{time}</h1>
      <h3 className="dateContainer">Date: {date}</h3>
    </>
  );
};

export default DigiClock;
