- 错误: TAG 在 FragmentActivity 中是 private 访问控制

```
public static final  String TAG="MainActivity"; //需要在class开头指定TAG
Log.d(TAG, "onStop");
```

