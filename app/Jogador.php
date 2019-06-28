<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Jogador extends Model
{
    protected $table = 'jogadors';
    protected $PrimaryKey = 'id';
    protected $fillable = ['nome','time','estado_origem','pais_origem'];
    public $timestamps = false;
}