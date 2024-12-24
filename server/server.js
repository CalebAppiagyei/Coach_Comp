const express = require("express");
const cors = require("cors");

const app = express();

app.use(express.json());
app.use(cors());

app.get("/test", (req, res) => {
    console.log(req.query)
    res.send("Request Received");
});

app.listen(4000, () => console.log("Server on localhost:4000"));