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


// TimesController
Route::group([
    'middleware' => 'api',
    'prefix' => 'jogador'
], function ($router) {
    Route::get('/', 'JogadorController@index')->name('index'); /*  http://localhost:8000/api/jogador/      */
    Route::post('store/', 'JogadorController@store')->name('store'); /*	http://localhost:8000/api/jogador/store/?nome=Riquelme&time=Vitoria&estado_origem=Pernambuco&pais_origem=Brasil */
    Route::get('show/{id}', 'JogadorController@show')->name('show'); /*	http://localhost:8000/api/jogador/show/1 */
    Route::put('update/{id}', 'JogadorController@update')->name('update'); /*	http://localhost:8000/api/jogador/update/1?nome=Paulo&time=Ceara&estado_origem=Bahia&pais_origem=Brasil */
    Route::delete('destroy/{id}', 'JogadorController@destroy')->name('destroy'); /* http://localhost:8000/api/jogador/destroy/1 */    
    Route::delete('deleteAll/', 'JogadorController@deleteAll')->name('deleteAll'); /*	http://localhost:8000/api/jogador/destroy/1 */    
});
   

// JogadorController
Route::group([
    'middleware' => 'api',
    'prefix' => 'times'
], function ($router) {
    Route::get('/', 'TimesController@index')->name('index'); /*  http://localhost:8000/api/times/      */
    Route::post('store/', 'TimesController@store')->name('store'); /*	http://localhost:8000/api/times/store/?nome=futebol */
    Route::get('show/{id}', 'TimesController@show')->name('show'); /*	http://localhost:8000/api/times/show/1 */
    Route::put('update/{id}', 'TimesController@update')->name('update'); /*	http://localhost:8000/api/times/update/1?nome=basquete */
    Route::delete('destroy/{id}', 'TimesController@destroy')->name('destroy'); /*	http://localhost:8000/api/times/destroy/1 */
});
    


