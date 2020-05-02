from multiprocessing import Process, Pipe


def show(conn):
    conn.send('Pipe 用法')
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    pro = Process(target=show, args=(child_conn,))
    pro.start()
    print(parent_conn.recv())
    pro.join()

    print(id(parent_conn))

