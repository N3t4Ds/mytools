import pandas as pd
import glob

def merge_excel_files(directory, output_file):
    all_dfs= []
    for excel_file in glob.glob(f"{directory}/*.xlsx"):
        df=pd.read_excel(excel_file)
        df['Source'] =excel_file  # 添加来源文件标识
        all_dfs.append(df)
    
    # 合并所有数据框
    merged_df=pd.concat(all_dfs, ignore_index=True)
    
    # 保存到新的Excel文件
    merged_df.to_excel(output_file, index=False)
    print(f"已将{len(all_dfs)}个Excel文件合并到{output_file}")
if __name__ == '__main__':

    # 使用示例
    merge_excel_files("./monthly_reports", "annual_report.xlsx")