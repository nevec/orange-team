package com.example.admin.try2;


import android.app.Activity;
import android.os.Bundle;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;


public class Test extends Activity {
    RadioGroup radioGroup;
    RadioButton radioButton;
    TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.test_activity);
/*        radioGroup = findViewById(R.id.radio1);
        textView = findViewById(R.id.text1);
        Button buttonApply = findViewById(R.id.button1);
        buttonApply.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int radioId = radioGroup.getCheckedRadioButtonId();

                radioButton = findViewById(radioId);

                if( radioButton.getId() == R.id.r1 )
                    textView.setText("you are weak");
                if( radioButton.getId() == R.id.r2 )
                    textView.setText("you are middle");
                if( radioButton.getId() == R.id.r3 )
                    textView.setText("you are strong");


            }
        });
        */
    }
}