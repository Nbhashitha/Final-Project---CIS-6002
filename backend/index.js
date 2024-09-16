const express = require("express");
const app = express();
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const cors = require("cors");
const path = require("path");
require("dotenv").config();

const PORT = process.env.PORT || 3420;

app.use(
  cors({
    origin: "*",
  })
);

// Middleware configuration
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, "/public")));
app.use("/static", express.static(path.join(__dirname, "/public/assets")));
app.use("/static", express.static(path.join(__dirname, "/admin")));
app.use("/static", express.static(path.join(__dirname, "/admin/assets")));

const urlDB =
  "mongodb+srv://" +
  process.env.DB_USERNAME +
  ":" +
  process.env.DB_PWD +
  "@rickets.tkbav.mongodb.net/ricketsDB?retryWrites=true&w=majority";

// database connections
mongoose
  .connect(urlDB, { useNewUrlParser: true }, { useUnifiedTopology: false })
  .then(() => {
    console.log("DB Connected");
  })
  .catch((err) => {
    console.log(JSON.stringify(err));
  });

// Root Route
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "/public/index.html"));
});

// Dashboard Route
app.get("/dashboard", (req, res) => {
  res.sendFile(path.join(__dirname, "/admin/index.html"));
});

// import routes
const registerRoute = require("./routes/userService/register");
const loginRoute = require("./routes/userService/login");
const userRoute = require("./routes/userService/user");
const postRoute = require("./routes/post/newPost");
const postViewRoute = require("./routes/post/view");

// use routes
app.use("/api/register", registerRoute);
app.use("/api/login", loginRoute);
app.use("/api/user", userRoute);
app.use("/api/newPost", postRoute);
app.use("/api/post", postViewRoute);

//listening from the server
app.listen(PORT, () => {
  console.log(`Server Running on ${PORT}`);
});