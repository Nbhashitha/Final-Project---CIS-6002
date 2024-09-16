const express = require("express");
const router = express.Router();
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
require("dotenv").config();

const User = require("../../models/Register");

router.get("/", async (req, res) => {
  res.send("Register Route");
});

router.post("/", async (req, res) => {
  const userName = req.body.userName;
  const pwd = req.body.password;

  if (!userName || typeof userName !== "string") {
    return res
      .status(400)
      .json({ status: "error", error: "Invalid user name" });
  }

  if (!pwd || typeof pwd !== "string") {
    return res
      .status(400)
      .json({ status: "error", error: "Invalid user name" });
  }

  if (pwd.length < 8) {
    return res.status(400).json({
      status: "error",
      error: "Password should be at least 8 characters",
    });
  }

  const hashedPassword = await bcrypt.hash(pwd, 10);

  let nameOfTheUser = req.body.firstName + " " + req.body.lastName;
 
  const register = new User({
    userName: req.body.userName,
    password: hashedPassword,
    name: nameOfTheUser,
    firstName: req.body.firstName,
    lastName: req.body.lastName,
    email: req.body.email,
  });

  try {
    const result = await register.save();
    const webToken = jwt.sign(
      {
        userName: register.userName,
      },
      process.env.JWT_SECRET
    );

    res.status(201).json({
      status: "200 OK",
      token: webToken,
      message: "User created Successfully",
      result: {
        userName: result.userName,
        name: result.name,
        Status: result.AccountStatus,
        email: result.email,
        address: result.address,
        phoneNumber: result.phoneNumber,
        isVerified: result.isVerified,
        userType: result.userType,
      },
    });
  } catch (err) {
    if (err.code === 11000) {
      return res.status(400).json({
        error: err,
        errorMessage: err.message,
        message: "User Name Duplication Error",
      });
    }
    return res.status(400).json({
      error: err.error,
      errorMessage: err.message,
      message: "Error while creating the user",
    });
  }
});

module.exports = router;
