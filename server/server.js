const express = require("express");
const cors = require("cors");
const pool = require("./database")

const app = express();

app.use(express.json());
app.use(cors());

app.get("/test", (req, res) => {
    console.log(req.query)
    res.send("Request Received");
});

app.post("/test", (req, res) => {
    const year = req.body["year"];
    const games = req.body["games_played"];

    console.log("Year: " + year);
    console.log("Games played: " + games);

    const query = {
        text: `INSERT INTO coach_schema.seasons (year, games_played) VALUES ($1, $2);`,
        values: [year, games]
    }
    pool.query(query).then((response) => {
        console.log("Season added");
        console.log(response);
    })
    .catch((err) => {
        console.log(err);
    });

    console.log(req.body);
    res.send("Response Received: " + req.body);
})

app.listen(4000, () => console.log("Server on localhost:4000"));