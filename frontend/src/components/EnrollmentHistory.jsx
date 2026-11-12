
export default function EnrollmentHistory({
    data,
    loading,
    error,
    onPageChange
}) {
    // 1. Đang tải dữ liệu
    if (loading) {
        return (
            <section className="panel">
                <h2>4. Lịch sử đăng ký</h2>
                <p>Đang tải lịch sử...</p>
            </section>
        );
    }

    // 2. Có lỗi khi tải dữ liệu
    if (error) {
        return (
            <section className="panel">
                <h2>4. Lịch sử đăng ký</h2>
                <p className="notice error">{error}</p>
            </section>
        );
    }

    // 3. Không có lịch sử
    if (!data || data.items.length === 0) {
        return (
            <section className="panel">
                <h2>4. Lịch sử đăng ký</h2>
                <p>Sinh viên chưa có lịch sử đăng ký.</p>
            </section>
        );
    }

    // 4. Hiển thị danh sách lịch sử
    return (
        <section className="panel">

            <h2>4. Lịch sử đăng ký</h2>

            <p className="muted">
                Tổng số sự kiện: {data.total}
            </p>

            <div className="table-scroll">
                <table>
                    <thead>
                        <tr>
                            <th>Mã sự kiện</th>
                            <th>Mã lớp</th>
                            <th>Loại sự kiện</th>
                            <th>Nguồn</th>
                            <th>Thời gian</th>
                        </tr>
                    </thead>

                    <tbody>
                        {data.items.map((item) => (
                            <tr key={item.id}>

                                <td>{item.id}</td>

                                <td>
                                    {item.class_section_id}
                                </td>

                                <td>
                                    {item.event_type}
                                </td>

                                <td>
                                    {item.source}
                                </td>

                                <td>
                                    {item.occurred_at}
                                </td>

                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            {/* PHÂN TRANG */}
            <div className="history-pagination">

                <button
                    type="button"
                    className="secondary"
                    disabled={data.page <= 1}
                    onClick={() =>
                        onPageChange(data.page - 1)
                    }
                >
                    Trang trước
                </button>

                <span>
                    Trang {data.page} / {data.total_pages}
                </span>

                <button
                    type="button"
                    disabled={data.page >= data.total_pages}
                    onClick={() =>
                        onPageChange(data.page + 1)
                    }
                >
                    Trang sau
                </button>

            </div>

        </section>
    );
}
