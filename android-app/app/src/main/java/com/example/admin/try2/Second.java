package com.example.admin.try2;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;


public class Second extends Activity{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.second_activity);
    }

    public void Map(View view) {
        //Создаем переход:
        Intent intent=new Intent(Second.this,MapsActivity.class);
        //Запускаем его при нажатии:
        startActivity(intent);
    }
    public void Test(View view) {
        //Создаем переход:
        Intent intent=new Intent(Second.this,Test.class);
        //Запускаем его при нажатии:
        startActivity(intent);
    }
    public void Add(View view){
        //Создаем переход:
        Intent intent=new Intent(Second.this,newmeeting.class);
        //Запускаем его при нажатии:
        startActivity(intent);
    }



}