<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Jogo extends Model
{
    protected $table = 'jogos';
    protected $PrimaryKey = 'id';
    protected $fillable = [
        'nome'
    ];
    public $timestamps = false;
}
