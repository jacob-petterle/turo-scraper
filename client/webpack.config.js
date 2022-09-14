import path from 'path';


module.exports = {
  //...
  resolve: {
    root: path.resolve(__dirname),
    extensions: [".ts", ".js"],
    alias: {
      features: ["src/features/"]
    }
  },
};