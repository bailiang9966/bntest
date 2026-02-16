import requests
import time

def get_btc_1h_futures_kline():
    """获取币安BTC/USDT永续合约1小时K线数据，返回最后一条"""
    # 币安合约K线API地址
    url = "https://fapi.binance.com/fapi/v1/klines"
    
    # 请求参数
    params = {
        "symbol": "BTCUSDT",    # BTC/USDT永续合约
        "interval": "1h",       # 1小时级别
        "limit": 10             # 获取最近10条，方便取最后一条
    }
    
    try:
        # 发送请求（添加超时和重试机制，避免网络波动）
        response = requests.get(
            url,
            params=params,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}  # 模拟浏览器请求，避免被拦截
        )
        # 检查API返回状态码
        response.raise_for_status()
        
        # 解析JSON数据
        kline_data = response.json()
        
        # 检查数据是否为空
        if not kline_data:
            print("错误：未获取到K线数据")
            return None
        
        # 取最后一条数据
        last_kline = kline_data[-1]
        
        # 格式化输出（K线数据字段说明：时间戳、开盘价、最高价、最低价、收盘价、成交量等）
        print("BTC/USDT 1小时合约最后一条K线数据：")
        print(f"时间戳: {last_kline[0]} (北京时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_kline[0]/1000 + 28800))})")
        print(f"开盘价: {last_kline[1]}")
        print(f"最高价: {last_kline[2]}")
        print(f"最低价: {last_kline[3]}")
        print(f"收盘价: {last_kline[4]}")
        print(f"成交量: {last_kline[5]}")
        
        return last_kline
    
    except requests.exceptions.Timeout:
        print("错误：请求超时，请检查网络或币安API状态")
        return None
    except requests.exceptions.RequestException as e:
        print(f"错误：网络请求失败 - {str(e)}")
        return None
    except Exception as e:
        print(f"错误：解析数据失败 - {str(e)}")
        return None

if __name__ == "__main__":
    # 执行获取K线函数
    get_btc_1h_futures_kline()
