package com.example.tengyuzhou.my_application;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Build;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import com.amazonaws.mobileconnectors.lambdainvoker.*;
import com.amazonaws.auth.CognitoCachingCredentialsProvider;
import com.amazonaws.regions.Regions;
import android.os.AsyncTask;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;
import android.widget.Toast;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        String s1 = "<a href=\"http://ec2-54-158-208-108.compute-1.amazonaws.com:5010\">Link 1</a>";
        final TextView mTextView = findViewById(R.id.textView);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            // flags
            // FROM_HTML_MODE_COMPACT：html块元素之间使用一个换行符分隔
            // FROM_HTML_MODE_LEGACY：html块元素之间使用两个换行符分隔
             mTextView.setText(Html.fromHtml(s1, Html.FROM_HTML_MODE_COMPACT));
        } else {
            mTextView.setText(Html.fromHtml(s1));
        }
        mTextView.setMovementMethod(LinkMovementMethod.getInstance());





//        Storing the phone number of children and the elder
        SharedPreferences sharedPref = this.getPreferences(Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPref.edit();
        String phone1 = sharedPref.getString("phone1", "0");
        String phone2 = sharedPref.getString("phone2", "0");
        Toast.makeText(MainActivity.this,"应用被打开了："+phone1+"次",Toast.LENGTH_LONG).show();
        Toast.makeText(MainActivity.this,"应用被打开了："+phone2+"次",Toast.LENGTH_LONG).show();



        CognitoCachingCredentialsProvider cognitoProvider = new CognitoCachingCredentialsProvider(
                this.getApplicationContext(),"us-east-1:cde1f481-491a-4105-ac3e-e05004d35af5", Regions.US_EAST_1);
        LambdaInvokerFactory factory = new LambdaInvokerFactory(this.getApplicationContext(),
                Regions.US_EAST_1, cognitoProvider);
        final MyInterface myInterface = factory.build(MyInterface.class);
        final RequestClass request = new RequestClass("John", "Doe", phone1, phone2);
// The Lambda function invocation results in a network call.
// Make sure it is not called from the main thread.
//        new AsyncTask<RequestClass, Void, ResponseClass>() {
//            @Override
//            protected ResponseClass doInBackground(RequestClass... params) {
//                // invoke "echo" method. In case it fails, it will throw a
//                // LambdaFunctionException.
//                try {
//                    return myInterface.suibianyige(params[0]);
//                } catch (LambdaFunctionException lfe) {
//                    Log.e("Tag", "Failed to invoke echo", lfe);
//                    return null;
//                }
//            }
//
//            @Override
//            protected void onPostExecute(ResponseClass result) {
//                if (result == null) {
//                    return;
//                }
//
//                // Do a toast
//                Toast.makeText(MainActivity.this, result.getGreetings(), Toast.LENGTH_LONG).show();
//            }
//        }.execute(request);


        final Button button2 = findViewById(R.id.button2);
        button2.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                new AsyncTask<RequestClass, Void, ResponseClass>() {
                    @Override
                    protected ResponseClass doInBackground(RequestClass... params) {
                        // invoke "echo" method. In case it fails, it will throw a
                        // LambdaFunctionException.
                        try {
                            return myInterface.suibianyige(params[0]);
                        } catch (LambdaFunctionException lfe) {
                            Log.e("Tag", "Failed to invoke echo", lfe);
                            return null;
                        }
                    }

                    @Override
                    protected void onPostExecute(ResponseClass result) {
                        if (result == null) {
                            return;
                        }

                        // Do a toast
                        Toast.makeText(MainActivity.this, result.getGreetings(), Toast.LENGTH_LONG).show();
                    }
                }.execute(request);
            }
        });
        final Button button3 = findViewById(R.id.button3);
        button3.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                new AsyncTask<RequestClass, Void, ResponseClass>() {
                    @Override
                    protected ResponseClass doInBackground(RequestClass... params) {
                        // invoke "echo" method. In case it fails, it will throw a
                        // LambdaFunctionException.
                        try {
                            return myInterface.suibianyige(params[0]);
                        } catch (LambdaFunctionException lfe) {
                            Log.e("Tag", "Failed to invoke echo", lfe);
                            return null;
                        }
                    }

                    @Override
                    protected void onPostExecute(ResponseClass result) {
                        if (result == null) {
                            return;
                        }

                        // Do a toast
                        Toast.makeText(MainActivity.this, result.getGreetings(), Toast.LENGTH_LONG).show();
                    }
                }.execute(request);
            }
        });

    }
    public void SavePhone(View button) {
        final EditText nameField1 = (EditText) findViewById(R.id.editText);
        String phone1 = nameField1.getText().toString();
        final EditText nameField2 = (EditText) findViewById(R.id.editText);
        String phone2 = nameField2.getText().toString();
        SharedPreferences sharedPref = this.getPreferences(Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPref.edit();
        editor.putString("phone1", phone1);
        editor.commit();
        editor.putString("phone2", phone2);
        editor.commit();
        Toast.makeText(MainActivity.this,"应用被打开了："+"次",Toast.LENGTH_LONG).show();
    }

}
