module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    proxy: {
      '^/ws': {
        target: 'http://localhost:5000',
        ws: true,
        changeOrigin: true
      },
    }
  }
}
