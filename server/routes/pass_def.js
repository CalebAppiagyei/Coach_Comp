const express = require('express');
const router = express.Router();
const pool = require("../database");

router.get("/pass_defense", async (req, res) => {
    console.log("Getting pass defenses");

    const query = {
        text: `SELECT * FROM coach_schema.pass_def_data`,
        values: []
    };

    try {
        const response = await pool.query(query)

        if (response.rows.length === 0) {
            console.log("No pass defense data")
            return res.status(404).json({message: "Defenses not found"});
        }

        console.log("Returning defenses")
        return res.status(200).json({
            message: "Defenses retrieved succesfully",
            coaches: response.rows,
        });
    }
    catch (err) {
        console.error("Error grabbing defenses from database:", err);
        return res.status(500).json({ error: "Error getting defenses"});
    }
});

router.post();

router.put();

router.delete();

module.exports = router;
