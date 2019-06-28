<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Time extends Model
{
    protected $table = 'times';
    protected $PrimaryKey = 'id';
    protected $fillable = ['nome','criador','estado','divisao'];
    public $timestamps = false;
}