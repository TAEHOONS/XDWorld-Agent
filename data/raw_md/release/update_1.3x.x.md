# - API 변경 내용 -

## 추가 API

> -   1.39.0 업데이트 내용 참조
> -   1.38.0 업데이트 내용 참조
> -   1.37.35 업데이트 내용 참조
> -   1.37.33 업데이트 내용 참조
> -   1.37.29 업데이트 내용 참조

## 샌드박스 업데이트

> -   [DEM 경사 조정](http://sandbox.dtwincloud.com/code/main.do?id=terrain_slope_rate)
> -   [카메라 경로 가시화](http://sandbox.dtwincloud.com/code/main.do?id=camera_move_path_visualize)

# - 업데이트 내역 -

## 1.39.0 (2022/12/14)

> -   wmts 하이브리드 로드 오류 수정
> -   타겟 오브제그트 이동 API 추가.

```
-   api : void moveTarget(object options)
-   class : JSTraceTarget
-   parameter
    -   options : 오브젝트 이동 방향 (front : 전진, back : 후진, left : 왼쪽, right : 오른쪽, up : 상승, down : 하강)
-   Example : trace.moveTarget({ left: 0.1, front: 0.1, up: 0.5});
```

> -   오브젝트 위치를 지형과 결합 API 추가.

```
-   api : void unionTargetToTerrain()
-   class : JSTraceTarget
```

## 1.38.0 (2022/12/07)

> -   개선 된 기능
>     -   [화면 분할 시 POI 라인이 단독 렌더링되는 현상 수정](https://github.com/EgisCorp/XDWorld/issues/230)
>     -   [중복키 이벤트 처리 추가](https://github.com/EgisCorp/XDWorld/issues/218)
>     -   [화면 분할 시 POI 라인이 단독 렌더링되는 현상 수정](https://github.com/EgisCorp/XDWorld/issues/230)
>     -   JSGridAnal 클래스에 단일 시간 분석 그리드 객체에 대한 표출기능 추가
>     -   마우스 클릭지점 이격 오류 수정

> 1. 레이어 별 클릭 지점 및 선택 오브젝트 리턴 API.

```
-   name : object pick(unsinged int screenX, unsigned int screenY)
-   class : JSLayer
-   parameter
    -   screenX : 화면 x 좌표
    -   screenY : 화면 y 좌표
-   return : 피킹 지점이 없는 경우 null 반환, 피킹 지점이 있는 경우 충돌한 오브젝트 키와 위치 좌표 반환함
-   참고 : (https://github.com/EgisCorp/XDWorld/issues/224)
```

> 2. JSObject 내 오브젝트 속성 정보 저장 및 반환 기능.

```
-   api : bool setProperty(string name, number/string value)
-   class : JSObject
-   parameter
    -   name : 속성 구분 이름
    -   value : 속성 값 (문자, 숫자 정보만 저장 가능)
-   return : 설정 성공 여부

-   api : number/string getProperty(string name)
-   class : JSObject
-   parameter
    -   name : 속성 구분 이름
-   return : 저장한 속성 값 (속성 값이 존재하지 않는 경우 null 반환)
```

> 3. Round 자동이동 위치 세그먼트 설정 프로퍼티 추가.
>
>     - JSCamera 클래스 내 autoMoveRoundSegment 프로퍼티가 추가됨.
>     - 기존 setAutoMoveRoundPositions API는 500개의 고정 된 이동 경로 점을 반환하였으나, autoMoveRoundSegment 파라미터를 통해 이동 경로 지점 수를 설정 가능하도록 수정됨.
>     - 세그먼트 수가 적을 수록 지점 간격이 넓어져 이동 속도가 빨라짐.

> 4. 3D 그리드 애니메이션 메쉬의 기준 높이 설정 API 추가.

```
-   api : void setBaseAltitude(float fAlt)
-   지정된 해발고도를 기준높으로 3d 그리드 표현을 시작
-   class : JSGridAnal
-   parameter
    -   fAlt : 기준 높이 값
```

> 5.  그리드 범례 절대값 설정 API 추가.

```
-   api : void setLegendMode(int _nMode)
-   class : JSGridAnal
-   parameter
    -   _nMode : 그리드 범례 절대값
        -   0 : 상대값 (%) 적용
        -   1 : 절대값 (val) 적용

-   api : bool setLegendJSON(object _options)
-   class : JSGridAnal
-   parameter
    -   _options : 설정 속성 값
        -   입력형식 { legendMode : Number, legend : [ { val : Number, color : { a, r, g, b ] }, { val : Number, color : { a, r, g, b ] }, ...] }
-   setLegendMode 및 컬러테이블 설정
```

> 6. JSGridAnal 클래스 내 단일 시간 다중 분석 그리드 객체에 대한 병합기능 추가.

```
-   api : void openMultipleGridDataURL(string szURL, unsigned int nTime, unsigned int nStripSize, unsigned int nStripStart, unsigned int nStripEnd, unsigned char nDataType, unsigned char nMultipleCnt, unsigned char nMultipleIndex)
-   class : JSGridAnal
-   parameter
    -   szURL : 데이터 요청 URL
    -   nTime : 시간 인덱스 (0-base)
    -   nStripSize : 그리드 하나의 셀의 byte 크기
    -   nStripStart : 그리드 셀에서 데이터 인식 offset 시작 byte (0-base)
    -   nStripEnd : 그리드 셀에서 데이터 인식 offset 종료 byte (0-base), nStripEnd - nStripStart가 데이터 바이트 크기
    -   nDataType : 데이터 자료형 (0 : int, 1 : float, 2 : double)
    -   nMultipleCnt : 다중 중첩 수
    -   nMultipleIndex : 다중 중첩 인덱스
-   그리드 필드 하나에 연결된 모든 데이터 필드를 합산하여 표현
```

> 7. JSGridAnal 클래스 내 마우스 클릭시 격자 정보 콜백기능 추가.

```
-   api : void setMouseCallback(function _callback)
-   그리드 데이터 로드후 마우스 왼쪽버튼을 통한 버튼 업에서 지정된 콜백 호출
-   class : JSGridAnal
-   parameter
    -   _callback : 콜백 함수
        -   콜백 반환 인자 : { longitude : Number, latitude : Number, idx : Number, idy : Number, value : Number , angle : Number }
```

> 8. JSGridAnal 클래스 내 격자 3D 라인 출력기능 추가.

```
-   api : void setGridLineVisible(boolean _visible)
-   그리드 라인 표현 여부 설정
-   class : JSGridAnal
-   parameter
    -   _visible : 가시화 설정 값

-   api : void setGridLineBaseAlt(float _fAltitude)
-   그리드 라인의 기준 표현 해발고도 설정
-   class : JSGridAnal
-   parameter
    -   _fAltitude : 기준 표현 해발고도

-   api : void setGridLineMaxDistance(float _fDistance)
-   그리드 라인의 최대 표현 해발고도, 최대표현부터 기준고도까지 거리별(%)로 알파 적용
-   class : JSGridAnal
-   parameter
    -   _fDistance : 그리드 라인의 최대 표현 해발고도
```

> 9. Canvas style left, top 옵션에 따른 마우스 위치 처리 기능 추가.

```
-   api : void ApplyCanvasPosition()
-   Canvas style 변경 시 동기화 실행
-   Canvas 위치 변경에 따른 HTMLObject 위치 조정 적용
-   class : Module
```

> 10. JSColorGrid 투명도 조절 API 추가.

```
-   api : void setOpacity(float _opacity)
-   class : JSColorGrid
-   parameter
    -   _opacity : 투명도 (0.0~1.0 사이 값 적용)
```

> 11. JSColorPolygon 투명도 조절 API 추가.

```
-   api : void setOpacity(float _opacity)
-   class : JSColorPolygon
-   parameter
    -   _opacity : 투명도 (0.0~1.0 사이 값 적용)
```

## 1.37.43 (2022/12/1)

> -   카메라 회전 예외 처리 추가

## 1.37.42 (2022/11/28)

> -   [이슈#223](https://github.com/EgisCorp/XDWorld/issues/223) 해결

## 1.37.41 (2022/11/25)

> -   지형그리드 생성 모듈 수정

## 1.37.40 (2022/11/18)

> -   HTMLObject 정렬 기능에 따른 위치 조정 기능 추가
> -   Real3D 단면도 출력 API 추가
> -   카메라 지하 이동 시 고정 배경 색상 지정 부분 수정
> -   2D 바 그래프 소수점 자릿수 설정 기능 추가
> -   값이 0인 2D 바 그래프 수치 텍스트 표시

## 1.37.39 (2022/10/31)

> -   객체 투명도 편집 오류 수정

## 1.37.38 (2022/10/26)

> -   객체 Fill, Stroke 모드 오류 수정

## 1.37.37 (2022/10/21)

> -   RTT Line 투명값 수정되지 않는 현상 수정

## 1.37.36 (2022/10/20)

> -   마우스 선택 모드에서 오브젝트가 선택되지 않는 현상 수정

## 1.37.35 (2022/10/12)

> -   JSLayer에 횡단면 출력 기능 사용 여부 설정 API setReal3dCutUse 추가
> -   JSLayer에 횡단면 출력 기능 높이 설정 API setReal3dCutHeight 추가

## 1.37.33 (2022/10/06)

> -   JSFlowPolygon 좌표 정보 반환 프로퍼티 'coordinates' 추가
> -   포인트-라인 간 최단 거리 계산 API getClosestPositionOnPath 추가

## 1.37.32 (2022/10/05)

> -   JSFlowPolygon/JSPolygon 오브젝트 선택 오류 수정
> -   바람길 기능 수정
>     -   빌딩관련 NoData 값 변경( 999 -> 0 )
>     -   토지피복도 관련 기능 추가

## 1.37.31 (2022/09/30)

> -   wfs poi, poi 인코딩 문제 수정

## 1.37.30 (2022/09/26)

> -   JSBarGraph3D 텍스트 텍스쳐 렌더링 오류 수정

## 1.37.29 (2022/09/23)

> -   메뉴얼 업데이트 JSTerrain, JSMath
> -   Module.getTerrain().makeTerrainElevationCellData("parameter") 추가
>     -   그리드 생성 기능
> -   Module.getMath().calculationSlopeAnalysis("parameter") 추가
>     -   [3 * 3] 배열값을 통한 경사 분석 기능
> -   Module.getMap().ScreenToMapPointEX API 실행 시 피킹점이 없는 경우 null 반환하도록 루틴 추가([이슈#211](https://github.com/EgisCorp/XDWorld/issues/211))

## 1.37.28 (2022/09/22)

> -   비디오 텍스쳐 Zoom In/Out 기능 추가
> -   버텍스 및 인덱스가 활용 된 JSColorPolygon의 마우스 피킹 기능 수정
> -   3D POI 텍스트의 문자 셋 지정 프로퍼티 추가

```javascript
var layerList = new Module.JSLayerList(false);
var layer = layerList.nameAtLayer("POI 텍스트 타일 레이어 이름");
layer.text_character_set = "EUC-KR"; // 디폴트 셋은 UTF-8
```

## 1.37.27 (2022/09/14)

> -   JSColorPolygon의 마우스 피킹 기능 추가

## 1.37.26 (2022/09/02)

> -   [이슈#203](https://github.com/EgisCorp/XDWorld/issues/203) 해결

## 1.37.23 (2022/08/24)

> -   비디오 텍스쳐 메모리 누수 관련 오류 수정
> -   [비디오텍스쳐](http://sandbox.dtwincloud.com/code/main.do?id=object_video_texture)
> -   [전광판](http://sandbox.dtwincloud.com/code/main.do?id=object_ledboard)

## 1.37.22 (2022/08/23)

> -   터치 이동/회전/줌인&아웃 사용 설정 프로퍼티 추가([이슈 200](https://github.com/EgisCorp/XDWorld/issues/200))

```javascript
// 터치 이동 활성화(true), 비활성화(false)
Module.getControl().touchPanEnable = true;

// 터치 회전 활성화(true), 비활성화(false)
Module.getControl().touchRotateEnable = true;

// 터치 줌 인&아웃 활성화(true), 비활성화(false)
Module.getControl().touchZoomEnable = true;
```

## 1.37.21 (2022/08/19)

> -   setDescription, getDescription uft16 지원([이슈 197](https://github.com/EgisCorp/XDWorld/issues/197))

## 1.37.20 (2022/08/04)

> -   고스트심볼(JSGhostSymbol) z버퍼 off 프로퍼티 추가([이슈 194](https://github.com/EgisCorp/XDWorld/issues/194))

```javascript
var object = Module.createGhostSymbol("MY_OBJECT");
object.zBufferOff = true;
```

## 1.37.19 (2022/08/04)

> -   건물 객첵 key List 기반 색상 변경 API 추가

## 1.37.18 (2022/08/02)

> -   실시간 cctv 관제 편집기능 추가

## 1.37.17 (2022/07/26)

> -   가시권 분석 이슈 처리([이슈 189](https://github.com/EgisCorp/XDWorld/issues/189))

## 1.37.16 (2022/07/19)

> -   입력된 영역과 객체의 영역 충돌 체크 조건 추가 (완전 포함, 조금이라도 포함)
> -   라이브맵 1차
> -   JSMap의 setSimpleMode API 오류 수정

## 1.37.15 (2022/07/13)

> -   레이어 별로 건물 심플 모드 설정이 가능한 JSLayer 프로퍼티 simple_real3d 추가

```javascript
var layerList = new Module.JSLayerList(false);
layer = layerList.nameAtLayer("building_layer_name");
layer.simple_real3d = true;
```

## 1.37.14 (2022/07/08)

> -   입력된 영역과 객체의 영역 충돌 체크 오류 수정

## 1.37.13 (2022/07/07)

> -   텍스쳐가 없는 Real3d의 색상 변경 API SetDefineMeshColorByObjectKey 미적용 오류 수정
> -   JSGhostSymbol의 API exportFileFormat에 XDO 텍스쳐 이미지 파일 지정 기능 추가

## 1.37.12 (2022/07/06)

> -   입력된 영역과 객체의 영역 충돌 체크 오류 수정
> -   그림자 분석, 비디오 텍스쳐 기능 오류 수정
