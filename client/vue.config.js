module.exports = {
  devServer: {
    proxy: "http://localhost:5000",
  },
  outputDir: "../server/dist/",
  assetsDir: "static",
  productionSourceMap: false,
};
