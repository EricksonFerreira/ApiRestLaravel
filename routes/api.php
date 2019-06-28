<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});
Route::group([
    'middleware' => 'api',
    'prefix' => 'jogos'
], function ($router) {
    Route::get('/', 'JogosController@index')->name('index'); /*  localhost:8000/api/jogos/      */
    Route::post('store/', 'JogosController@store')->name('store'); /*	localhost:8000/api/jogos/store/?nome=futebol */
    Route::get('show/{id}', 'JogosController@show')->name('show'); /*	localhost:8000/api/jogos/show/1 */
    Route::put('update/{id}', 'JogosController@update')->name('update'); /*	localhost:8000/api/jogos/update/1?nome=basquete */
    Route::delete('destroy/{id}', 'JogosController@destroy')->name('destroy'); /*	localhost:8000/api/jogos/destroy/1 */
});
    // Route::post('show', 'JogosController@show')->name('show');