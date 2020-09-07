const path = require("path");

module.exports = {
  outputDir: path.resolve(__dirname, "./templates"),
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    proxy: {
      '/info': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      },
    }
  }
}
