function submitEvent() {
    const fileInput = document.getElementById('midiFile');
    const button = document.getElementById('submitBtn');
    if (fileInput.files.length === 0) {
        alert('파일을 선택하세요.');
        return false;
    }

    // 로딩중 버튼 상태 변환
    button.innerHTML = '로딩중';
    button.disabled = true;

    return true;
}
