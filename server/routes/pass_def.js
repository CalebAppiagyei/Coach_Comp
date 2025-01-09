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

// POST method for adding pass defense data
router.post("/pass_defense", async function (req, res) {
    const {
        team_id,
        completions = 0,
        attempts = 0,
        yards = 0,
        touchdowns = 0,
        interceptions = 0,
        nya = 0,
        first_downs = 0,
    } = req.body;

    if (!team_id) {
        return res.status(400).json({ error: "Missing team ID" });
    }

    const query = {
        text: `
            INSERT INTO coach_schema.pass_def_data 
            (team_id, completions, attempts, yards, touchdowns, interceptions, nya, first_downs)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8) 
            RETURNING *;
        `,
        values: [team_id, completions, attempts, yards, touchdowns, interceptions, nya, first_downs],
    };

    try {
        const response = await pool.query(query);
        return res.status(201).json({
            message: "Pass defense data added successfully",
            data: response.rows[0],
        });
    } catch (err) {
        console.error("Error adding pass defense data:", err);
        return res.status(500).json({ error: "Error adding pass defense data" });
    }
});

// PUT method for updating pass defense data
router.put("/pass_defense/:team_id", async (req, res) => {
    const { team_id } = req.params;
    const {
        completions,
        attempts,
        yards,
        touchdowns,
        interceptions,
        nya,
        first_downs,
    } = req.body;

    if (
        completions === undefined &&
        attempts === undefined &&
        yards === undefined &&
        touchdowns === undefined &&
        interceptions === undefined &&
        nya === undefined &&
        first_downs === undefined
    ) {
        return res.status(400).json({ error: "Missing fields to update" });
    }

    // Build the dynamic query
    const fields = [];
    const values = [];
    let idx = 1;

    if (completions !== undefined) {
        fields.push(`completions = $${idx++}`);
        values.push(completions);
    }
    if (attempts !== undefined) {
        fields.push(`attempts = $${idx++}`);
        values.push(attempts);
    }
    if (yards !== undefined) {
        fields.push(`yards = $${idx++}`);
        values.push(yards);
    }
    if (touchdowns !== undefined) {
        fields.push(`touchdowns = $${idx++}`);
        values.push(touchdowns);
    }
    if (interceptions !== undefined) {
        fields.push(`interceptions = $${idx++}`);
        values.push(interceptions);
    }
    if (nya !== undefined) {
        fields.push(`nya = $${idx++}`);
        values.push(nya);
    }
    if (first_downs !== undefined) {
        fields.push(`first_downs = $${idx++}`);
        values.push(first_downs);
    }

    values.push(team_id);

    const query = {
        text: `
            UPDATE coach_schema.pass_def_data 
            SET ${fields.join(", ")} 
            WHERE team_id = $${idx} 
            RETURNING *;
        `,
        values: values,
    };

    try {
        const response = await pool.query(query);

        if (response.rows.length === 0) {
            return res.status(404).json({ error: "Team not found" });
        }

        return res.status(200).json({
            message: "Pass defense data updated successfully",
            data: response.rows[0],
        });
    } catch (err) {
        console.error("Error updating pass defense data:", err);
        return res.status(500).json({ error: "Error updating pass defense data" });
    }
});

// DELETE method for removing pass defense data
router.delete("/pass_defense/:team_id", async (req, res) => {
    const { team_id } = req.params;

    if (!team_id) {
        return res.status(400).json({ error: "Missing team ID" });
    }

    const query = {
        text: `DELETE FROM coach_schema.pass_def_data WHERE team_id = $1`,
        values: [team_id],
    };

    try {
        const response = await pool.query(query);

        if (response.rowCount === 0) {
            return res.status(404).json({ error: "Team not found" });
        }

        return res.status(200).json({
            message: "Pass defense data successfully removed",
        });
    } catch (err) {
        console.error("Error deleting pass defense data:", err);
        return res.status(500).json({ error: "Error removing pass defense data" });
    }
});


module.exports = router;
