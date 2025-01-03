require('dotenv').config();
const {Pool} = require("pg")

const pool = new Pool({
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    database: process.env.DB
})

pool.query("SELECT * FROM information_schema.tables WHERE table_schema = 'coach_schema';").then((res) => {
    console.log("Grabbing all tables within schema");
    console.log(res);
}).catch((err) => {
    console.log(err);
});

module.exports = pool;