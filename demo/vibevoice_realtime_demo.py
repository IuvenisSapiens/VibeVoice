import argparse
import os
import threading
import webbrowser
import uvicorn

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=3000)
    p.add_argument("--model_path", type=str, default="./VibeVoice-Realtime-0.5B")
    p.add_argument("--device", type=str, default="cuda", choices=["cpu", "cuda", "mpx", "mps"])
    p.add_argument("--reload", action="store_true", help="Reload the model or not")
    args = p.parse_args()
    
    os.environ["MODEL_PATH"] = args.model_path
    os.environ["MODEL_DEVICE"] = args.device
    url = f"http://127.0.0.1:{args.port}"
    def open_browser():
        # 等待一段时间以确保服务器启动完成
        import time
        time.sleep(20)  # 调整等待时间以适应您的服务器启动速度
        webbrowser.open(url)
    # 启动浏览器的线程
    threading.Thread(target=open_browser).start()
    uvicorn.run("web.app:app", host="127.0.0.1", port=args.port, reload=args.reload)

if __name__ == "__main__":
    main()
