# EasyExcel 简单使用

EasyExcel是阿里巴巴开源的一个excel处理框架，**以使用简单、节省内存著称**。EasyExcel能大大减少占用内存的主要原因是在解析Excel时没有将文件数据一次性全部加载到内存中，而是从磁盘上一行行读取数据，逐个解析。

git地址：https://github.com/alibaba/easyexcel

快速开始：https://www.yuque.com/easyexcel/doc/easyexcel

特点：

- EasyExcel采用一行一行的解析模式，并将一行的解析结果以观察者的模式通知处理（AnalysisEventListener）。

### 简单使用

> 引入依赖

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>easyexcel</artifactId>
    <version>2.1.7</version>
</dependency>
```

> 创建相关实体类

```java
@Data
public class ExcelStudentDTO {

    @ExcelProperty("姓名")
    private String name;

    @ExcelProperty("生日")
    private Date birthday;

    @ExcelProperty("薪资")
    private Double salary;
}
```

> 简单读

```java
public class ExcelReadTest {

    @Test
    public void simpleReadXlsx() {
        String fileName = "d:/simpleWrite.xlsx";
        EasyExcel.read(fileName, ExcelStudentDTO.class, new ExcelStudentDTOListener()).sheet().doRead();
    }

    @Test
    public void simpleReadXls() {
        String fileName = "d:/simpleWrite.xls";
        EasyExcel.read(fileName, ExcelStudentDTO.class, new ExcelStudentDTOListener()).excelType(ExcelTypeEnum.XLS).sheet().doRead();
    }
}
```

> 简单写

写的测试方法

```java
public class ExcelWriteTest {

    @Test
    public void simpleWriteTestXlsx() {
        String fileName = "d:/simpleWrite.xlsx";
        EasyExcel.write(fileName, ExcelStudentDTO.class).sheet("模板").doWrite(data());
    }

    @Test
    public void simpleWriteTestXls() {
        String fileName = "d:/simpleWrite.xls";
        EasyExcel.write(fileName, ExcelStudentDTO.class).excelType(ExcelTypeEnum.XLS).sheet("模板").doWrite(data());
    }

    //辅助方法
    private List<ExcelStudentDTO> data(){
        List<ExcelStudentDTO> list = new ArrayList<>();

        //算上标题，做多可写65536行
        //超出：java.lang.IllegalArgumentException: Invalid row number (65536) outside allowable range (0..65535)
        for (int i = 0; i < 10; i++) {
            ExcelStudentDTO data = new ExcelStudentDTO();
            data.setName("Matuto" + i);
            data.setBirthday(new Date());
            data.setSalary(123456.1234);
            list.add(data);
        }
        return list;
    }
}
```

写的监听类：

```java
@Slf4j
public class ExcelStudentDTOListener extends AnalysisEventListener<ExcelStudentDTO> {
    // 该方法解析一条数据调用一次
    @Override
    public void invoke(ExcelStudentDTO excelStudentDTO, AnalysisContext analysisContext) {
        log.info("解析到一条记录：{}", excelStudentDTO.toString());
    }

    // 文件全部数据解析完成后进行调用
    @Override
    public void doAfterAllAnalysed(AnalysisContext analysisContext) {
        log.info("解析完全部数据");
    }
}
```

注：针对不同的Excel版本，EasyExcel提供了不同的读写方法，注意区分。

###实战用法 

```java
@Slf4j
@NoArgsConstructor
public class ExcelDictDTOListener extends AnalysisEventListener<ExcelDictDTO> {

    private DictMapper dictMapper;

    // 数据列表
    List<ExcelDictDTO> list = new ArrayList<>();

    // 临界值 - 一次处理多少数据
    private static final int BATCH_COUNT = 5;

    public ExcelDictDTOListener(DictMapper dictMapper) {
        this.dictMapper = dictMapper;
    }

    @Override
    public void invoke(ExcelDictDTO data, AnalysisContext analysisContext) {
        log.info("解析到一条数据：{}", data);

        // 将数据存入数据列表
        list.add(data);
        if (list.size() >= BATCH_COUNT) {
            // 调用mapper层的save方法
            saveData();
            list.clear();
        }
    }

    @Override
    public void doAfterAllAnalysed(AnalysisContext analysisContext) {
        // 当最后剩余的数据记录数不足 BATCH_COUNT 时，我们最终一次性存储剩余数据
        saveData();
        log.info("读取全部数据");
    }

    private void saveData() {
        log.info("{} 条数据被存储到数据库......", list.size());
        // 调用mapper 层的批量save方法：save list对象
        // TODO
        dictMapper.insertBatch(list);
        log.info("{} 条数据被存储到数据库成功！", list.size());
    }
}
```
