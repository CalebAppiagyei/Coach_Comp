const express = require('express');
const router = express.Router();
const pool = require("../database");

router.get("/coaches", async (req, res) => {
    console.log("Getting coaches");

    const query = {
        text: `SELECT * FROM coach_schema.coach_data`,
        values: []
    };

    try {
        const response = await pool.query(query)

        if (response.rows.length === 0) {
            console.log("No coaches")
            return res.status(404).json({message: "Coaches not found"});
        }

        console.log("Returning coaches")
        return res.status(200).json({
            message: "Coaches retrieved succesfully",
            coaches: response.rows,
        });
    }
    catch (err) {
        console.err("Error grabbing coaches from database:", err);
        return res.status(500).json({ error: "Error getting coaches"});
    }
});

router.post();

router.put();

router.delete();

module.exports = router;

