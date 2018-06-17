package com.example.admin.try2;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;


public class newmeeting extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.newmeeting_activity);
        TextView a, b;
        a = (TextView) findViewById(R.id.editText11);
        b = (TextView) findViewById(R.id.editText12);
        int a0, b0;
        a0 = Integer.parseInt(a.toString());
        b0 = Integer.parseInt(b.toString());


    }



}