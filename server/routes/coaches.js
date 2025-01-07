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
        console.error("Error grabbing coaches from database:", err);
        return res.status(500).json({ error: "Error getting coaches"});
    }
});

router.post("/coaches", async function (req, res) {
    const name = req.body.name;
    const games = req.body.games ?? 0;
    const wl_pct = req.body.wl_pct ?? 0;
    
    if (!name) {
        console.log("Missing coach name");
        return res.status(400).json({error: "Missing coach name"});
    }

    const query = {
        text: `INSERT INTO coach_schema.coach_data (name, games, wl_pct)
                VALUES ($1, $2, $3) RETURNING *;`,
        values: [name, games, wl_pct]
    };

    try {
        const response = await pool.query(query);
        return res.status(201).json({
            message: "Coach added succesfully",
            coach: response.rows[0]
        });
    }
    catch (err) {
        console.error("Error adding coach to database:", err);
        return res.status(500).json({error: "Error adding coach"});
    }
});

router.put("/coaches/:id", async (req, res) => {
    const coach_id = req.params.id;
    const { name, games, wl_pct } = req.body;

    if (!name || !games || !wl_pct) {
        return res.status(400).json({ error: "Missing required fields" });
    }

    // Build the update query dynamically based on provided fields
    const fields = [];
    const values = [];
    let idx = 1;

    if (name) {
        fields.push(`name = $${idx++}`);
        values.push(name);
    }
    if (games) {
        fields.push(`games = $${idx++}`);
        values.push(games);
    }
    if (wl_pct) {
        fields.push(`wl_pct = $${idx++}`);
        values.push(wl_pct);
    }

    values.push(coach_id);

    const query = {
        text: `UPDATE coach_schema.coach_data 
               SET ${fields.join(", ")} 
               WHERE coach_id = $${idx} 
               RETURNING *;`,
        values: values,
    };

    try {
        const response = await pool.query(query);

        if (response.rows.length === 0) {
            return res.status(404).json({ error: "Coach not found" });
        }

        return res.status(200).json({
            message: "Coach updated successfully",
            coach: response.rows[0],
        });
    } catch (err) {
        console.error("Error updating coach:", err);
        return res.status(500).json({ error: "Error updating coach" });
    }
});

router.delete("/coaches/:id", async (req, res) => {
    const coach_id = req.params.id;

    if (!coach_id) {
        return res.status(400).json({ error: "Missing coach ID" });
    }
    
    const query = {
        text: `DELETE FROM coach_schema.coach_data WHERE coach_id = $1`,
        values: [coach_id]
    };

    try {
        const response = await pool.query(query);

        if (response.rowCount === 0) {
            return res.status(404).json({ error: "Coach not found" });
        }
        
        return res.status(200).json({
            message: "Successfully removed coach"
        });
    }
    catch (err) {
        console.log("Error deleting coach");
        return res.status(500).json({error: "Error removing coach"});
    }
});

module.exports = router;

