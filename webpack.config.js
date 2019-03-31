const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const devMode = process.env.NODE_ENV !== 'production';
const CopyWebpackPlugin = require('copy-webpack-plugin');


module.exports = {
    context: __dirname,
    entry: devMode ? './assets/js/index' : './staticfiles/js/index',
    output: {
        path: devMode ? path.resolve('./assets/dist/') : path.resolve('./staticfiles/dist/'),
        filename: 'js/app.js'
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new VueLoaderPlugin(),
        new MiniCssExtractPlugin({
          filename: 'css/app.css',
          chunkFilename: '[id].css'
        }),
        new CopyWebpackPlugin([
            { from: 'node_modules/@fortawesome/fontawesome-free/webfonts', to: './webfonts'}
        ])
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
                 // 'postcss-loader',
                 "sass-loader"
                ]
            }
        ]
    },
    resolve: {
        alias: {vue: 'vue/dist/vue.js'}
    },

};
