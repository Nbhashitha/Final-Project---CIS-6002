const mongoose = require("mongoose");

const registerSchema = mongoose.Schema(
  {
    userName: {
      type: "string",
      required: true,
      unique: true,
    },
    password: {
      type: "string",
      required: true,
    },
    name: {
      type: "string",
      required: true,
    },
    firstName: {
      type: "string",
      required: true,
    },
    lastName: {
      type: "string",
      required: true,
    },
    email: {
      required: true,
      type: "string",
    },
  },
  { collection: "Users" }
);

module.exports = mongoose.model("User", registerSchema);
