# 반경 측정

마우스 모드를 반경 측정 모드로 변경한 후 클릭 지점 반경을 측정합니다.

첫번째 클릭 지점은 중점이 되고 두번째 클릭 지점까지 거리를 구하여 반지름을 형성합니다.

측정결과 값을 이벤트로 반환 받아 POI로 가시화 합니다.

![](../.gitbook/assets/radius.png)

## 기능 구현

#### Symbol

이미지 텍스쳐를 저장하는 텍스쳐 맵 오브젝트를 이 곳에 저장합니다.

[JSSymbol](../object/jssymbol.md)에 대한 간략한 설명은 거리 측정 튜토리얼의 [step 5. 거리 객체 생성](tutorial\_distance.md#step-5.) 항목의 JSSymbol 설명을 참조하세요.

#### POILayer

생성한 [JSPoint](../object/jspoint.md) 오브젝트를 저장할 레이어를 이 변수에 저장합니다.

레이어를 저장하는 과정은 [step 1.레이어 생성](tutorial\_radius.md#step-1.) 단계를 참조하세요.

#### WallLayer

반경을 구분하는 벽면 폴리곤을 저장하는 레이어 입니다.

레이어를 저장하는 과정은 [step 1.레이어 생성](tutorial\_radius.md#step-1.) 단계를 참조하세요.

<details>

<summary>위 기능을 구현하는 전체 코드입니다.</summary>

```javascript
/* 엔진 로드 후 실행할 초기화 함수(Module.postRun) */
function init() {

	Module.Start(window.innerWidth, window.innerHeight);

	 // 카메라 위치 설정
	Module.getViewCamera().setLocation(new Module.JSVector3D(129.128265, 35.171834, 1000.0));
	
	 // 아이콘 관리 심볼 생성
	GLOBAL.Symbol = Module.getSymbol();

	// 분석 출력 POI 레이어 생성
	var layerList = new Module.JSLayerList(true);
	GLOBAL.POILayer = layerList.createLayer("MEASURE_POI", Module.ELT_3DPOINT);
	GLOBAL.POILayer.setMaxDistance(20000.0);
	GLOBAL.POILayer.setSelectable(false);
	
	GLOBAL.WallLayer = layerList.createLayer("MEASURE_WALL", Module.ELT_POLYHEDRON);
	GLOBAL.WallLayer.setMaxDistance(20000.0);
	GLOBAL.WallLayer.setSelectable(false);
	GLOBAL.WallLayer.setEditable(true);
	
	initEvent(Module.canvas);
}

var GLOBAL = {
    Symbol : null,		// 아이콘 관리 심볼 객체
    POILayer : null,		// POI 저장 레이어
    WallLayer : 0			// POI, Icon 생성 인덱스
};

/* 이벤트 설정 */
function initEvent(canvas) {

	// 반경 이벤트 설정
	canvas.addEventListener("Fire_EventAddRadius", function(e){		
		if(e.dTotalDistance > 0) {
			// POI 오브젝트 삭제
			clearIcon();
			
			// 반경 POI 오브젝트 생성
			createPOI( new Module.JSVector3D(e.dMidLon, e.dMidLat, e.dMidAlt), "rgba(255, 204, 198, 0.8)", e.dTotalDistance, true );
		}
	});
}

/* 마우스 상태 변경 */
function setMouseState(_option){

    // 마우스 모드 설정
    Module.XDSetMouseState(_option);
}

/* 분석 내용 출력 POI 생성 */
function createPOI(_position, _color, _value, _balloonType) {

	// POI 아이콘 이미지를 그릴 Canvas 생성
	var drawCanvas = document.createElement('canvas');
    drawCanvas.width = 100;
    drawCanvas.height = 100;

	// 아이콘 이미지 데이터 반환
	var imageData = drawIcon(drawCanvas, _color, _value, _balloonType);

	// 심볼에 아이콘 이미지 등록
	if (GLOBAL.Symbol.insertIcon("Icon", imageData, drawCanvas.width, drawCanvas.height)) {

		// 등록한 아이콘 객체 반환
		var icon = GLOBAL.Symbol.getIcon("Icon");

		// JSPoint 객체 생성
		var poi = Module.createPoint("POI");

		poi.setPosition(_position);		// 위치 설정
		poi.setIcon(icon);				// 아이콘 설정

		// 레이어에 오브젝트 추가
		GLOBAL.POILayer.addObject(poi, 0);
	}
}

/* 아이콘 이미지 데이터 반환 */
function drawIcon(_canvas, _color, _value, _balloonType) {

	// 컨텍스트 반환 및 배경 초기화
	var ctx = _canvas.getContext('2d'),
		width = _canvas.width,
		height = _canvas.height
		;
	ctx.clearRect(0, 0, width, height);

	// 배경 Draw Path 설정 후 텍스트 그리기
	if (_balloonType) {
		drawBalloon(ctx, height*0.5, width, height, 5, height*0.25, _color);
		setText(ctx, width*0.5, height*0.2, _value);
	} else {
		drawRoundRect(ctx, 0, height*0.3, width, height*0.25, 5, _color);
		setText(ctx, width*0.5, height*0.5, _value);
	}

	return ctx.getImageData(0, 0, _canvas.width, _canvas.height).data;
}

/* 말풍선 배경 그리기 */
function drawBalloon(ctx,
					 marginBottom, width, height,
					 barWidth, barHeight,
					 color) {

	var wCenter = width * 0.5,
		hCenter = height * 0.5;

	// 말풍선 형태의 Draw Path 설정
	ctx.beginPath();
	ctx.moveTo(0, 				 0);
	ctx.lineTo(0, 				 height-barHeight-marginBottom);
	ctx.lineTo(wCenter-barWidth, height-barHeight-marginBottom);
	ctx.lineTo(wCenter, 		 height-marginBottom);
	ctx.lineTo(wCenter+barWidth, height-barHeight-marginBottom);
	ctx.lineTo(width,			 height-barHeight-marginBottom);
	ctx.lineTo(width,			 0);
	ctx.closePath();

	// 말풍선 그리기
	ctx.fillStyle = color;
    ctx.fill();
}

/* 둥근 사각형 배경 그리기 */
function drawRoundRect(ctx,
					   x, y,
					   width, height, radius,
					   color) {

	if (width < 2 * radius) 	radius = width * 0.5;
	if (height < 2 * radius) 	radius = height * 0.5;

	ctx.beginPath();
	ctx.moveTo(x+radius, y);
	ctx.arcTo(x+width, 	y, 	 		x+width, 	y+height, 	radius);
	ctx.arcTo(x+width, 	y+height, 	x,		 	y+height, 	radius);
	ctx.arcTo(x, 	 	y+height, 	x,   		y,   		radius);
	ctx.arcTo(x,	   	y,   	 	x+width, 	y,   		radius);
	ctx.closePath();

	// 사각형 그리기
	ctx.fillStyle = color;
    ctx.fill();

	return ctx;
}

/* 텍스트 그리기 */
function setText(_ctx, _posX, _posY, _value) {

	var strText = "";

	// 텍스트 문자열 설정
	if (typeof _value == 'number') {
		strText = setKilloUnit(_value, 0.001, 0);
	} else {
		strText = _value;
	}

	// 텍스트 스타일 설정
	_ctx.font = "bold 16px sans-serif";
    _ctx.textAlign = "center";
	_ctx.fillStyle = "rgb(0, 0, 0)";

	// 텍스트 그리기
    _ctx.fillText(strText, _posX, _posY);
}

/* m/km 텍스트 변환 */
function setKilloUnit(_text, _meterToKilloRate, _decimalSize){

	if (_decimalSize < 0){
		_decimalSize = 0;
	}
	if (typeof _text == "number") {
		if (_text < 1.0/(_meterToKilloRate*Math.pow(10,_decimalSize))) {
			_text = _text.toFixed(1).toString()+'m';
		} else {
			_text = (_text*_meterToKilloRate).toFixed(2).toString()+'㎞';
		}
	}
	return _text;
}

/* 분석 내용 초기화 */
function clearAnalysis() {

	// 실행 중인 분석 내용 초기화
	Module.XDClearCircleMeasurement();

	if (GLOBAL.WallLayer == null) {
		return;
	}

	// icon 삭제
	clearIcon();

	// POI 오브젝트 삭제
	GLOBAL.WallLayer.removeAll();
}

/* icon 초기화 */
function clearIcon() {

	if (GLOBAL.POILayer == null) {
		return;
	}

	// 등록된 아이콘 리스트 삭제
	var icon, poi;

	poi = GLOBAL.POILayer.keyAtObject("POI");
	
	if (poi == null) {
		return;
	}
	
	icon = poi.getIcon();

	// 아이콘을 참조 중인 POI 삭제
	GLOBAL.POILayer.removeAtKey("POI");

	// 아이콘을 심볼에서 삭제
	GLOBAL.Symbol.deleteIcon(icon.getId());
}
```

</details>

이어서 코드의 세부 단계에 대해 알아봅니다.



### step 1. 레이어 생성

반경 측정 Icon 및 반경 값을 가시화 할 레이어를 생성합니다.

레이어 타입에 대한 설명은 [여기](../etc/type-list.md)를 참조해 주십시오.

```javascript
var layerList = new Module.JSLayerList(true);

GLOBAL.POILayer = layerList.createLayer("MEASURE_POI", Module.ELT_3DPOINT);
GLOBAL.POILayer.setMaxDistance(20000.0);
GLOBAL.POILayer.setSelectable(false);

GLOBAL.WallLayer = layerList.createLayer("MEASURE_WALL", Module.ELT_POLYHEDRON);
GLOBAL.WallLayer.setMaxDistance(20000.0);
GLOBAL.WallLayer.setSelectable(false);
GLOBAL.WallLayer.setEditable(true);
```



### step 2. 이벤트 등록

엔진 내부에서 계산된 반경을 반환 받기 위해 이벤트를 등록합니다.

```javascript
function initEvent(canvas) {

    // 반경 이벤트 설정
    canvas.addEventListener("Fire_EventAddRadius", function(e){		
        if(e.dTotalDistance > 0) {
            // 반경 POI 오브젝트 생성
            createPOI( new Module.JSVector3D(e.dMidLon, e.dMidLat, e.dMidAlt), "rgba(255, 204, 198, 0.8)", e.dTotalDistance );
        }
    j});
}
```

Fire\_EventAddRadius 이벤트는 마우스 모드가 MML\_ANALYS\_AREA\_CIRCLE일 경우 발생합니다.



### step 3. 마우스모드 변경

반경 측정을 위해서 마우스 모드를 변경합니다.

마우스 모드에 대한 설명은 [여기](../etc/type-list.md)를 참조해 주십시오.

```javascript
Module.XDSetMouseState(Module.MML_ANALYS_AREA_CIRCLE);
```



### step 4 - 1. 반경 Icon 생성

반환 받은 반경 값을 랜더링 하기 위해 Icon을 생성합니다.

```javascript
function drawIcon(_canvas, _color, _value) {

    // 컨텍스트 반환 및 배경 초기화
    var ctx = _canvas.getContext('2d'),
        width = _canvas.width,
        height = _canvas.height
        ;
    ctx.clearRect(0, 0, width, height);

    // 배경 Draw Path 설정 후 텍스트 그리기
    drawBalloon(ctx, height*0.5, width, height, 5, height*0.25, _color);
    setText(ctx, width*0.5, height*0.2, _value);
	
    return ctx.getImageData(0, 0, _canvas.width, _canvas.height).data;
}
```

맨 처음 이미지를 그릴 canvas를 생성하고, 글자를 작성할 배경을 칠한 후([step 4-2. 반경 말풍선 Icon 생성](tutorial\_radius.md#step-4-2.-icon))

반환 된 고도 값을 토대로 텍스트를 입력합니다. ([step 4-3. 반경 측정 결과 값 Icon 생성](tutorial\_radius.md#step-4-3.-icon))



### step 4 - 2. 반경 말풍선 Icon 생성

반환 받은 반경 값을 가시화 할 말풍선을 캔버스에 그립니다.

```javascript
function drawBalloon(ctx,  marginBottom, width, height, barWidth, barHeight, color) {

    var wCenter = width * 0.5,
        hCenter = height * 0.5;

    // 말풍선 형태의 Draw Path 설정
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, height-barHeight-marginBottom);
    ctx.lineTo(wCenter-barWidth, height-barHeight-marginBottom);
    ctx.lineTo(wCenter, height-marginBottom);
    ctx.lineTo(wCenter+barWidth, height-barHeight-marginBottom);
    ctx.lineTo(width, height-barHeight-marginBottom);
    ctx.lineTo(width, 0);
    ctx.closePath();

    // 말풍선 그리기
    ctx.fillStyle = color;
    ctx.fill();
}
```



### step 4 - 3. 반경 측정 결과 값 Icon 생성

반환 받은 반경 값을 말풍선 위에 텍스트로 그립니다.

```javascript
function setText(_ctx, _posX, _posY, _value) {

    var strText = "";

    // 텍스트 문자열 설정
    if (typeof _value == 'number') {
        strText = setKilloUnit(_value, 0.001, 0);
    } else {
        strText = _value;
    }

    // 텍스트 스타일 설정
    _ctx.font = "bold 16px sans-serif";
    _ctx.textAlign = "center";
    _ctx.fillStyle = "rgb(0, 0, 0)";

    // 텍스트 그리기
    _ctx.fillText(strText, _posX, _posY);
}
```



### step 4 - 4. 반경 측정 단위(m/km) 텍스트 변환

반환 받은 반경 값을 m/km 텍스트로 변환합니다.

```javascript
function setKilloUnit(_text, _meterToKilloRate, _decimalSize){

    if (_decimalSize < 0){
        _decimalSize = 0;
    }
    if (typeof _text == "number") {
        if (_text < 1.0/(_meterToKilloRate*Math.pow(10,_decimalSize))) {
            _text = _text.toFixed(1).toString()+'m';
        } else {
            _text = (_text*_meterToKilloRate).toFixed(2).toString()+'㎞';
        }
    }
    return _text;
}
```



### step 5. 반경 객체 생성

생성한 Icon으로 객체를 만들고 레이어에 추가합니다.

```javascript
function createPOI(_position, _color, _value) {

    // POI 아이콘 이미지를 그릴 Canvas 생성
    var drawCanvas = document.createElement('canvas');
    drawCanvas.width = 100;
    drawCanvas.height = 100;

    // 아이콘 이미지 데이터 반환
    var imageData = drawIcon(drawCanvas, _color, _value);

    // 심볼에 아이콘 이미지 등록
    if (GLOBAL.Symbol.insertIcon("Icon", imageData, drawCanvas.width, drawCanvas.height)) {

        // 등록한 아이콘 객체 반환
        var icon = GLOBAL.Symbol.getIcon("Icon");

        // JSPoint 객체 생성
        var poi = Module.createPoint("POI");

        poi.setPosition(_position);    // 위치 설정
        poi.setIcon(icon);    // 아이콘 설정
        
        // 레이어에 오브젝트 추가
        GLOBAL.POILayer.addObject(poi, 0);
    }
}
```



### step 6. 반경 측정 초기화

반경 측정 결과 및 객체를 초기화합니다.

```javascript
function clearAnalysis() {

    // 실행 중인 분석 내용 초기화
    Module.XDClearCircleMeasurement();

    if (GLOBAL.WallLayer == null) {
        return;
    }

    // icon 삭제
    if (GLOBAL.POILayer == null) {
        return;
    }

    // 등록된 아이콘 리스트 삭제
    var icon, poi;

    poi = GLOBAL.POILayer.keyAtObject("POI");
	
    if (poi == null) {
        return;
    }
	
    icon = poi.getIcon();

    // 아이콘을 참조 중인 POI 삭제
    GLOBAL.POILayer.removeAtKey("POI");

    // 아이콘을 심볼에서 삭제
    GLOBAL.Symbol.deleteIcon(icon.getId());

    // POI 오브젝트 삭제
    GLOBAL.WallLayer.removeAll();
}
```

## 결과 화면

![](../.gitbook/assets/radius.png)

반경 측정 과정에 대한 라이브 코드를 확인해 보고 싶으시다면? [여기](http://sandbox.dtwincloud.com/code/main.do?id=analysis\_measure\_radius)를 클릭해 주세요
