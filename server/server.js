const express = require("express");
const cors = require("cors");
const pool = require("./database")
const bodyParser = require('body-parser')

const app = express();

app.use(express.json());
app.use(bodyParser.urlencoded({
    extended: true
  }));
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

const coachRoutes = require("./routes/coaches");
// const passDefRoutes = require("./routes/pass_def");
// const passOffRoutes = require("./routes/pass_off");
// const rushOffRoutes = require("./routes/rush_off");
// const rushDefRoutes = require("./routes/rush_def");
// const offRoutes = require("./routes/tot_off");
// const defRoutes = require("./routes/tot_def");
// const seasonRoutes = require("./routes/seasons");
// const teamRoutes = require("./routes/teams");

app.use('', coachRoutes);
// app.use('', passDefRoutes);
// app.use('', passOffRoutes);
// app.use('', rushOffRoutes);
// app.use('', rushDefRoutes);
// app.use('', offRoutes);
// app.use('', defRoutes);
// app.use('', seasonRoutes);
// app.use('', teamRoutes);

module.exports = app;
