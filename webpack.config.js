var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const devMode = process.env.NODE_ENV !== 'production'


module.exports = {
    context: __dirname,
    entry: './assets/js/index',
    output: {
        path: path.resolve('./assets/dist/'),
        filename: 'app.js'
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new VueLoaderPlugin(),
        new MiniCssExtractPlugin({
          filename: 'app.css',
          chunkFilename: '[id].css'
        })
    ],

    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.(sa|sc|c)ss$/,
                use: [
                 devMode ? 'style-loader' : MiniCssExtractPlugin.loader,
                 "css-loader",
                 "sass-loader"
                ]
            }
        ]
    },
    resolve: {
        alias: {vue: 'vue/dist/vue.js'}
    },

};