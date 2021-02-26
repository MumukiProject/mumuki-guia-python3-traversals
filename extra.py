import StringIO
import sys

def capture_stdout(block):
  out = start_capture()
  block()
  return end_capture(out)
  
def start_capture():
  out = StringIO.StringIO()
  sys.stdout = out
  return out

def end_capture(out):
  sys.stdout = sys.__stdout__
  return out.getvalue()