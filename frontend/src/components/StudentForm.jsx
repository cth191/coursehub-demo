export default function StudentForm({
    value,
    studentId,
    onChange,
    onSubmit,
    onRefresh,
    disabled,
    loading
}) {
    return (
        <section className="panel">

            <h2>1. Chọn sinh viên</h2>

            <form
                className="student-form"
                onSubmit={onSubmit}
            >
                <label htmlFor="student-id">
                    Mã sinh viên
                </label>

                <input
                    id="student-id"
                    value={value}
                    maxLength={8}
                    required
                    inputMode="numeric"
                    onChange={(e) =>
                        onChange(e.target.value)
                    }
                    disabled={disabled}
                />

                <button
                    type="submit"
                    disabled={disabled}
                >
                    Xem đăng ký
                </button>

                <button
                    type="button"
                    className="secondary"
                    disabled={disabled || loading}
                    onClick={onRefresh}
                >
                    Tải lại dữ liệu
                </button>

            </form>

            <p className="muted">
                Dữ liệu đang xem:
                {" "}
                <strong>{studentId}</strong>.

                {" "}Mã mẫu: 22000001–22000004.
            </p>

        </section>
    );
}