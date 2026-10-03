import express from "express";
import { question } from "../controllers/controllers.js";

const router = express.Router();

router.post("/query", question);

export default router;
