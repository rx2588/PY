import java.io.File;
import org.openqa.selenium.Cookie;
import java.util.*;
import java.io.*;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
  public static void main(String[] args) {
    for (String arg: args) {
      if (!arg.endsWith(".csv")) {
        continue;
      }

      // System.out.println(arg);

      try {
        List<Map<String, Set<Cookie>>> account = readSerAccFile(arg);
        // System.out.println(account.toString());

        // 将 对象转换为 JSON 字符串
        String json = JSON.toJSONString(account);
        String outputPath = arg.substring(0, arg.length() - 4) + ".json";

        // System.out.println(json);
        
        // 将 JSON 字符串写入文件
        FileWriter writer = new FileWriter(outputPath);
        writer.write(json);
        writer.flush();
        writer.close();

      } catch (Exception e) {
        System.out.println(e.toString());
      }
    }
  }

  private static List<Map<String, Set<Cookie>>> readSerAccFile (String path) {
		List<Map<String, Set<Cookie>>> account = null;

    try {
      FileInputStream fis = new FileInputStream(path);
      ObjectInputStream ois = new ObjectInputStream(fis);
      account = (List<Map<String, Set<Cookie>>>) ois.readObject();			
    } catch (Exception e) {
      // TODO: handle exception
      System.out.println("读取文件错误" + e.toString());
    }
			
		return account;
	}
}