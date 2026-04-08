---
description: Fire_이벤트 정리
---

# EVENT

## 기본 Event

> HTML Canvas 이벤트 등록으로 엔진과 연동되는 이벤트

```javascript
var canvas = document.createElement('canvas');
canvas.id = "canvas";
	
canvas.addEventListener("Fire_~~~~", function(e){
		// 기능 구현
});
```

| Index | Name                      | Description       |
| ----- | ------------------------- | ----------------- |
| 0     | Fire\_EventSelectedObject | 객체 선택 시 이벤트       |
| 1     | Fire\_EventRotateCompass  | 나침반 회전 시 이벤트      |
| 2     | Fire\_EventCameraMoveEnd  | 카메라 이동 종료 시 이벤트   |
| 3     | Fire\_JSEventResize       | 캔버스 리사이즈 시 이벤트    |
| 4     | Fire\_EventAddRadius      | 수직 평면 반경 생성 시 이벤트 |
| 5     | Fire\_EventAddDistancePoint      | 거리 측정 값 반환 시 이벤트 |
| 6     | Fire\_EventAddAreaPoint      | 면적 측정 값 반환 시 이벤트 |
| 7     | Fire\_EventAddAltitudePoint      | 높이 측정 값 반환 시 이벤트 |
| 8     | Fire\_EventFinishTransparencyAutoMove      | 터파기 자동 이동 종료 시 이벤트 |
| 9     | Fire\_EventCompleteShadowSimulation      | 일조 분석(그림자) 시뮬레이션 종료 시 이벤트 |

- 별도의 표기가 없는 경우, 해당 이벤트는 변수를 제공하지 않습니다.

### Fire_EventRotateCompass
|변수 이름 | 자료형 | 상세 설명|
| ----- | ------------------------- | ----------------- |
| dCameraHeadAngle | double | 나침반(네비게이션) 방향 각도(Degree) |

### Fire_EventAddDistancePoint
|변수 이름 | 자료형 | 상세 설명|
| ----- | ------------------------- | ----------------- |
| dDistance | double | 부분 측정 거리 값(이전 입력점과 마지막 입력점 간의 거리, m 단위) |
| dTotalDistance | double | 전체 측정 거리 값(첫 입력점과 마지막 입력점 간의 거리, m 단위) |
| dMidLon | double | 부분 측정 거리 값 표시 경도 (Degree 단위) |
| dMidLat | double | 부분 측정 거리 값 표시 위도 (Degree 단위) |
| dMidAlt | double | 부분 측정 거리 값 표시 고도 (m 단위) |
| dLon | double | 전체 측정 거리 값 표시 경도 (Degree 단위) |
| dLat | double | 전체 측정 거리 값 표시 위도 (Degree 단위) |
| dAlt | double | 전체 측정 거리 값 표시 고도 (m 단위) |
		
### Fire_EventAddAreaPoint
|변수 이름 | 자료형 | 상세 설명|
| ----- | ------------------------- | ----------------- |
| dArea | double | 면적 측정 값 (제곱 m 단위) |
| dLon | double | 면적 측정 표시 경도 (Degree 단위) |
| dLat | double | 면적 측정 표시 위도 (Degree 단위) |
| dAlt | double | 면적 측정 표시 고도 (m 단위) |

### Fire_EventAddAltitudePoint
|변수 이름 | 자료형 | 상세 설명|
| ----- | ------------------------- | ----------------- |
| dGroundAltitude | double | 해발 고도 측정 값 (m 단위) |
| dObjectAltitude | double | 지형에서 부터 선택 지점까지의 높이 측정 값 (m 단위) |
| dLon | double | 높이 측정 표시 경도(Degree 단위) |
| dLat | double | 높이 측정 표시 위도(Degree 단위) |
| dAlt | double | 높이 측정 표시 고도(m 단위) |

## Ghost Symbol Event

> 고스트 심볼 이벤트 등록으로 엔진과 연동되는 이벤트

```javascript
var canvas = document.createElement('canvas');
canvas.id = "canvas";
canvas.addEventListener("Fire_GhostSymbolRegistComplete", function(e){
		// 기능 구현
});

~
Module.getGhostSymbolMap().addGhostSymbolBy3DS()
~
	
```

| Index | Name                            | Description     |
| ----- | ------------------------------- | --------------- |
| 0     | Fire\_GhostSymbolRegistComplete | 고스트 심볼 등록 시 이벤트 |
