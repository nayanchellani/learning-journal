import React from "react";
import { useState } from "react";
import axios from "axios";
const Component = () => {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState("");

  function updateCity(e) {
    setCity(e.target.value);
  }
  async function getWeather() {
    try {
      const response = await axios.get(
        `http://localhost:5000/weather?city=${city}`
      );

      if (response.data.error) {
        setError("City not found");
        setWeather(null);
      } else {
        setWeather(response.data);
        setError("");
      }
    } catch (err) {
      setError("Server error");
      setWeather(null);
    }
  }

  return (
    <>
    
      <div className="container">
        <h1>WEATHER FORECAST</h1>
        <input
          placeholder="Enter city name"
          value={city}
          type="text"
          onChange={updateCity}
        ></input>

        <button onClick={getWeather}>SEARCH</button>
        {error && <h3>{error}</h3>}
        {weather && (
          <div>
            <h2>CITY : {weather.location.name}</h2>
            <h2> COUNTRY : {weather.location.country}</h2>
            <p>Weather state: {weather.current.condition.text}</p>
            <img src={weather.current.condition.icon} className="icon" alt="" />
            <h2 className="temp">TEMPERATURE: {weather.current.temp_c} °</h2>
          </div>
        )}
      </div>
    </>
  );
};

export default Component;
