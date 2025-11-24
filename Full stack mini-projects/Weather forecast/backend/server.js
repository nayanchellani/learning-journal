const express = require("express");
const cors = require("cors");
const axios = require("axios");

const app = express();
app.use(cors());

const API = "cfd0b710d8f24c82b96123651252211";

app.get("/weather", async (req, res) => {
    const city = req.query.city;

    const url = `https://api.weatherapi.com/v1/current.json?key=${API}&q=${city}`;

    try {
        const response = await axios.get(url);
        res.json(response.data);  

    } catch (error) {
        res.json({ error: "City not found" });
    }
});

app.listen(5000, () => {
    console.log("Backend running on http://localhost:5000");
});
